#include <stdio.h>  
#include <sys/time.h>
#include <sys/types.h>
#include <unistd.h>

#include <sys/stat.h> //open
#include <fcntl.h>

int main(int argc, char ** argv) {
  fd_set rfds;
  struct timeval tv;
  int retval;

  if (argc < 2) {
    fprintf(stderr,"provide a file name to monitor as an argument.\n");
    return -1;
  }
  char * fname = argv[1];
  int fd = open(fname,O_RDONLY);

  if (fd < 0) {
    fprintf(stderr,"could open file %s to monitor\n", fname);
    return -1;
  }

  /* Watch stdin (fd 0) to see when it has input. */
  FD_ZERO(&rfds);
  FD_SET(fd, &rfds);

  while (true) {
    /* Wait up to five seconds. */
    tv.tv_sec = 5;
    tv.tv_usec = 0;
    retval = select(1, &rfds, NULL, NULL, &tv);
    /* Don’t rely on the value of tv now! */

    if (retval == -1){
      perror("select()");
    } else if (retval) {
      printf("file is accessed now. \n");
    /* FD_ISSET(0, &rfds) will be true. */
    } else{
      printf("No data within five seconds.\n");
    }
  }
  close(fd);
  return 0;
}
