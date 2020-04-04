/*************************************************************************\
*                  Copyright (C) Michael Kerrisk, 2014.                   *
*                                                                         *
* This program is free software. You may use, modify, and redistribute it *
* under the terms of the GNU Affero General Public License as published   *
* by the Free Software Foundation, either version 3 or (at your option)   *
* any later version. This program is distributed without any warranty.    *
* See the file COPYING.agpl-v3 for details.                               *
\*************************************************************************/

/* demo_inotify.c

   Demonstrate the use of the inotify API.

   Usage: demo_inotify pathname...

   The program monitors each of the files specified on the command line for all
   possible file events.

   This program is Linux-specific. The inotify API is available in Linux 2.6.13
   and later.
*/
#include <sys/inotify.h>
#include <limits.h>
/*#include "tlpi_hdr.h"*/
#include <sys/types.h>  /* Type definitions used by many programs */
#include <stdio.h>      /* Standard I/O functions */
#include <stdlib.h>     /* Prototypes of commonly used library functions,
                                                      plus EXIT_SUCCESS and EXIT_FAILURE constants */
#include <unistd.h>     /* Prototypes for many system calls */
#include <errno.h>      /* Declares errno and defines error constants */
#include <string.h>     /* Commonly used string-handling functions */

#include <map>
#include <string>

using namespace std;

map<int,string> watchMap;
string command;
int inotifyFd;

void errExit(const char * m) {
  fprintf(stderr, m);
  exit(-1);
}

#define fatal errExit


static void             /* Display information from inotify_event structure */
displayInotifyEvent(struct inotify_event *i)
{
#if 1
    printf("    wd =%2d;%s ", i->wd, watchMap[i->wd].c_str());
    if (i->cookie > 0){
        printf("cookie =%4d; ", i->cookie);
    }

    printf("mask = ");
    if (i->mask & IN_ACCESS)        printf("IN_ACCESS ");
    if (i->mask & IN_ATTRIB)        printf("IN_ATTRIB ");
    if (i->mask & IN_CLOSE_NOWRITE) printf("IN_CLOSE_NOWRITE ");
    if (i->mask & IN_CLOSE_WRITE)   printf("IN_CLOSE_WRITE ");
    if (i->mask & IN_CREATE)        printf("IN_CREATE ");
    if (i->mask & IN_DELETE)        printf("IN_DELETE ");
    if (i->mask & IN_DELETE_SELF)   printf("IN_DELETE_SELF ");
    if (i->mask & IN_IGNORED)       printf("IN_IGNORED ");
    if (i->mask & IN_ISDIR)         printf("IN_ISDIR ");
    if (i->mask & IN_MODIFY)        printf("IN_MODIFY ");
    if (i->mask & IN_MOVE_SELF)     printf("IN_MOVE_SELF ");
    if (i->mask & IN_MOVED_FROM)    printf("IN_MOVED_FROM ");
    if (i->mask & IN_MOVED_TO)      printf("IN_MOVED_TO ");
    if (i->mask & IN_OPEN)          printf("IN_OPEN ");
    if (i->mask & IN_Q_OVERFLOW)    printf("IN_Q_OVERFLOW ");
    if (i->mask & IN_UNMOUNT)       printf("IN_UNMOUNT ");
    printf("\n");

    if (i->len > 0){
        printf("        name = %s\n", i->name);
    }
#endif
    if (i->mask & IN_CLOSE_WRITE || i->mask & IN_MOVE_SELF) {
#if 0
      if (i->len > 0) {
        printf("file %s had been written to and closed\n", i->name);
      }
#endif
      fprintf(stdout,"Executing command %s \n", command.c_str());

      system(command.c_str());
      if ( inotify_rm_watch(inotifyFd,i->wd) != 0 ) {
        fprintf(stderr,"could not remove watch from file %s\n", watchMap[i->wd].c_str());
      }
      int wd = inotify_add_watch(inotifyFd, watchMap[i->wd].c_str(),IN_ALL_EVENTS);
      if (wd == -1){
        errExit("inotify_add_watch");
      }
      watchMap[wd] = watchMap[i->wd];
    }
}

#define BUF_LEN (10 * (sizeof(struct inotify_event) + NAME_MAX + 1))



int
main(int argc, char *argv[])
{
    int wd, j;
    char buf[BUF_LEN] __attribute__ ((aligned(8)));
    ssize_t numRead;
    char *p;
    struct inotify_event *event;

    if (argc < 3 || strcmp(argv[1], "--help") == 0 ||  strcmp(argv[1], "-h")==0){
        fprintf(stderr, "%s file [files...] command\n", argv[0]);
        fprintf(stderr, "      watches `file' [and files] for a change and executes `command'.\n"
                        "      when a change happens. Uses inotify api for that.\n"
                        "      Currently it executes `command' on IN_CLOSE_WRITE and on IN_MOVE_SELF events.\n");
        exit(-1);
    }

    inotifyFd = inotify_init();                 /* Create inotify instance */

    if (inotifyFd == -1){
        errExit("inotify_init");
    }

    /* For each command-line argument, add a watch for all events */
    for (j = 1; j < argc -1; j++) {
        wd = inotify_add_watch(inotifyFd, argv[j], IN_ALL_EVENTS);
        if (wd == -1){
            errExit("inotify_add_watch");
        }
        watchMap[wd] = argv[j];
        printf("Watching %s using wd %d\n", argv[j], wd);
    }
    command = argv[argc-1];

    for (;;) {                                  /* Read events forever */
        numRead = read(inotifyFd, buf, BUF_LEN);
        if (numRead == 0){
            fatal("read() from inotify fd returned 0!");
        }

        if (numRead == -1){
            errExit("read");
        }

        printf("Read %ld bytes from inotify fd\n", (long) numRead);

        /* Process all of the events in buffer returned by read() */

        for (p = buf; p < buf + numRead; ) {
            event = (struct inotify_event *) p;
            displayInotifyEvent(event);

            p += sizeof(struct inotify_event) + event->len;
        }
    }

    exit(EXIT_SUCCESS);
}
