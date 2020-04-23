# Covid19
This repository is a fast prototype for a social media messaging based symptom tracker as a response for the spread of COVID-19. 
It should be useful in countries where a significant majority of data packages and internet penetration is limited to social media messaging. 

The main idea is to facilitate for users to send their symptoms through text or voice notes to the tracker. 
The prototype assumes use of WhatsApp is prevalant and a number of WhatsApp accounts are dedicated to collect the messages. 

The users send their messages to the designated WhatsApp contacts. 

The WASymTrack has a server (var/www/python) that implements the WhatsApp business API to collect the text messages and the urls of the voice notes. 
It also has a pull client that pulls the collected data into a local machine, and runds speech to text engine(s) over the collected voice notes. 
It also has a test directory to test tha APIs and the scripts. 

The Watcher is a file system based server that watches a directory for changes and processes the comma separated value files that the WASymTrack servers add to the directory. 
It sends these files to the extractor. 
The extractor aggregates the messages, applies NLP technqiues to extract the symptoms and inserts the results into a central DB for analytics. 

The prototype supports the Arabic language and makes use of third party alternative Arabic speech recognition systems (one is paid and one is kaldi based and open source).

The system was built after consultation with the Ministry of Public Health in Lebanon and several medical doctors at the American University of Beirut Medical center who thought the system is very beneficial and can guide the management of medical resources especially whem massive testing is not possible. 

