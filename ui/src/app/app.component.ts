import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders }  from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{

  title = 'ui';
  patients_invoices: any = []
    calendar: any = {
      0: {
       'MON': {'day': 26, 'appointments': []},
       'TUE': {'day': 27, 'appointments': []},
       'WED': {'day': 28, 'appointments': []},
       'THU': {'day': 29, 'appointments': []},
       'FRI': {'day': 30, 'appointments': []},
       'SAT': {'day': 31, 'appointments': []},
       'SUN': {'day': 1, 'appointments': []}
      },
      1: {
       'MON': {'day': 2, 'appointments': []},
       'TUE': {'day': 3, 'appointments': []},
       'WED': {'day': 4, 'appointments': []},
       'THU': {'day': 5, 'appointments': []},
       'FRI': {'day': 6, 'appointments': []},
       'SAT': {'day': 7, 'appointments': []},
       'SUN': {'day': 8, 'appointments': []}
      },
      2: {
       'MON': {'day': 9, 'appointments': []},
       'TUE': {'day': 10, 'appointments': []},
       'WED': {'day': 11, 'appointments': []},
       'THU': {'day': 12, 'appointments': []},
       'FRI': {'day': 13, 'appointments': []},
       'SAT': {'day': 14, 'appointments': []},
       'SUN': {'day': 15, 'appointments': []}
      },
      3: {
       'MON': {'day': 16, 'appointments': []},
       'TUE': {'day': 17, 'appointments': []},
       'WED': {'day': 18, 'appointments': []},
       'THU': {'day': 19, 'appointments': []},
       'FRI': {'day': 20, 'appointments': []},
       'SAT': {'day': 21, 'appointments': []},
       'SUN': {'day': 22, 'appointments': []}
      },
      4: {
       'MON': {'day': 23, 'appointments': []},
       'TUE': {'day': 24, 'appointments': []},
       'WED': {'day': 25, 'appointments': []},
       'THU': {'day': 26, 'appointments': []},
       'FRI': {'day': 27, 'appointments': []},
       'SAT': {'day': 28, 'appointments': []},
       'SUN': {'day': 29, 'appointments': []}
      },
      5: {
       'MON': {'day': 30, 'appointments': []},
       'TUE': {'day': 1, 'appointments': []},
       'WED': {'day': 2, 'appointments': []},
       'THU': {'day': 3, 'appointments': []},
       'FRI': {'day': 4, 'appointments': []},
       'SAT': {'day': 5, 'appointments': []},
       'SUN': {'day': 6, 'appointments': []}
      }
  }
  years = [2020, 2021]
  selectedYear=2020
  months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
            'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
  selectedMonth='Abril'

  newAppointmentName = null;
  newAppointmentValue = 30000;
  newAppointmentDate = null;
  newAppointmentTime = null;
  newAppointmentFrecuency = 0;
  newAppointmentEndDate = null;

  bearer = ''

  constructor(private http: HttpClient) { }

  ngOnInit(){

    this.selectedYear = this.thisYear()
    this.selectedMonth = this.thisMonth()

    let endpoint = "api/authentication"

    this.http.post(endpoint, {}).subscribe(apiData => {
      this.bearer = apiData['token']
      console.log(apiData)
      console.log(apiData['token'])

      let options = {
        headers: new HttpHeaders()
          .set('Authorization', 'Bearer ' + this.bearer)
      }
      this.http.get('api/generate_calendar?month='+ this.monthStringToInt(this.selectedMonth) +'&year=' + this.selectedYear, options).subscribe(apiData => {
        this.calendar = apiData;
      })

    })
  }

  private monthStringToInt(month){
    let months = {'Enero': 1, 'Febrero': 2, 'Marzo': 3, 'Abril': 4, 'Mayo': 5, 'Junio': 6, 'Julio': 7,
    'Agosto': 8, 'Septiembre': 9, 'Octubre': 10, 'Noviembre': 11, 'Diciembre': 12}
    return months[month]
  }

  private monthIntToString(month){
    let months = {1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio', 7: 'Julio',
    8: 'Agosto', 9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'}
    return months[month]
  }

  showAgenda(){
    let options = {
      headers: new HttpHeaders()
        .set('Authorization', 'Bearer ' + this.bearer)
    }
    this.http.get('api/generate_calendar?month='+ this.monthStringToInt(this.selectedMonth) +'&year='+this.selectedYear, options).subscribe(apiData => {
      this.calendar = apiData;
    })
  }

  scheduleAppointments(){

    let endpoint = 'api/create_appointment?repeat_until=' + this.newAppointmentEndDate + 
      '&every_number_of_weeks=' + this.newAppointmentFrecuency + 
      '&patient=' + this.newAppointmentName +
      '&cost=' + this.newAppointmentValue +
      '&date_time=' + this.newAppointmentDate + ' ' + this.newAppointmentTime
    let options = {
      headers: new HttpHeaders()
        .set('Authorization', 'Bearer ' + this.bearer)
    }
    this.http.post(endpoint, {}, options).subscribe(apiData => {
      this.http.get('api/generate_calendar?month='+ this.monthStringToInt(this.selectedMonth) +'&year='+this.selectedYear, options).subscribe(calendarData => {
        console.log(calendarData)
        this.calendar = calendarData;
      })
    })


  }

  generateInvoices(){

    let options = {
      headers: new HttpHeaders()
        .set('Authorization', 'Bearer ' + this.bearer)
    }
    this.http.get('api/generate_invoice?month='+ this.monthStringToInt(this.selectedMonth) + '&year=' + this.selectedYear, options).subscribe(apiData => {
      console.log(apiData['patients']);
      this.patients_invoices = apiData['patients']
    })

  }

  private thisYear(){
    return new Date().getFullYear()
  }
  
  private thisMonth(){
    return this.monthIntToString(new Date().getMonth()+1)
  }

}

