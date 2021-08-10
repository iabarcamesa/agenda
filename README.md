# My Agenda project

## About this project

### Why did I start this project?

I started this project for two reasons:

- I wanted to practice my coding skills implementing ideas from the [Clean Architecture](https://www.amazon.com/-/es/Martin-Robert-C-ebook-dp-B075LRM681/dp/B075LRM681/ref=mt_other?_encoding=UTF8&me=&qid=) book that I liked very much without having the time constraints of a real project, in other words I wanted to do it at my own pace.

- As I needed a reason (or an excuse) to do the first, I decided to help my partner (she is a speech therapist) with a system that helps her to calculate (and in the future generate) the monthly invoices for her patients.

### What does the system do?

- The system allows to schedule patients appointments with a defined price for each appointment (therapists generally schedule periodical appointments for their patients unlike physicians).

- The system has a simple calendar that shows for each day of the month which patients are appointed.

- The system allows to pseudo-generate invoices for each month: it generate a field for each patient with the day of each appointment and the monthly cost (this information is useful to generate the invoices faster in the invoice official system, but the idea is to integrate with it in the future and generate the invoices automatically).

### What does the system don't do?

A lot of things :( as it is a work in progress yet, but I want to improve it :)

Among other things what is missing is:

- An authentication logic. It can be used by only one user now.

- You can’t delete or change appointments.

- You can’t see the time of the appointment (so it doesn’t work as a scheduling system).

- You can’t administrate patients so the way of differentiating a patient from another is the full name.

- Probably many other things (but remember that the idea is to practice my development skills).

### In which technical concept I’m focusing now?

This may change as the project evolve but now I’m working on the concept that _“the database is a detail”_ so I intentionally started building the system storing the data in pickle files to defer the decision of using a database and when that time arrives it should be easy for me to implement any database without the need of modifying the existing code, if I achieve this I’ll be happy because it means that I improved my skills with this concept.

There is more information about the Clean Architecture concepts in [this blog](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html).

_**Disclaimer:** I’m aware that the current implementation of the persistence using pickle files is very very inefficient, in the best case O(n), but it’s not the idea that it should be efficient, the idea is that changing it with another persistence that have the same behaviour (and hopefully more efficient) will be easy._

## Running the project

### What do I need to run the project?

The back-end of the project is coded in Python (with Flask) and the front-end in Typescript (with Angular) and to deploy it I use Docker so what you need to have installed in your development environment is:

- Python
- Angular CLI
- Node
- Docker

### How do I run the project for development?

First you need to run the backend, so in a terminal do the following:

- Install python dependencies with the command: `pip install -r requirements.txt`
- Run the backend with the command: `python main.py`

This will start the backend in the port 5000 and you will be able to see the backend swagger documentation in http://127.0.0.1:5000/api/docs

Then you need to start the front-end, for this do the following:

- In another terminal go to the _ui_ folder doing `cd ui`, there you will find the Angular app of the front-end
- Start it with the command `ng serve` (you need to be in the _ui_ folder to run this command)

This will start the front-end in the port 4200 so you can see the application navigating to http://127.0.0.1:4200 and start using and modifying it.

When using the `ng serve` command the front-end app generates a proxy to the back-end app running in the 5000 port so it must be kept running.

### Does the project have tests?

Yes, but only for the backend (for now). You can find the tests in the _tests_ folder and if you want to understand how the code works first I recommend reading and understanding the tests.

Tu run the test just execute the script `tests.sh` typing `./tests.sh` in a terminal. (Don’t run the test doing only `pytest` because it won’t work because you need to ignore the Angular tests of the ui folder)

### Can I deploy the project in a production environment?

Yes, for this I use Docker, to build the container run the script `build.sh` typing `./build.sh` in a terminal, this will generate the agenda image and you can run it with the command `docker run -p 80:80 agenda` then you can navigate to http://127.0.0.1 and see the application. Also if you want you can deploy this image in your prefered Docker environment.

### If there is no database, how does the data persist?

To persist the data everything is stored in a pickle file in the folder named _data_ you will see that this folder is created after running the application for development or after running the tests.

If you want to persist the data when running the Docker image you have to attach a local volume in the containers _/data_ route, for this you have to run the container with the command `docker run -p 80:80 -v <local_folder>:/data agenda` where `<local_folder>` is the path of the local folder where you want to persist the pickle files.
