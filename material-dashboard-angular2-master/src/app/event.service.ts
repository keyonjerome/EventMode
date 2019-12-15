import { Injectable } from '@angular/core';
import { AngularFireDatabase, AngularFireObject, AngularFireList } from '@angular/fire/database';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { FrontPageComponent } from './front-page/front-page.component';

@Injectable({
  providedIn: 'root'
})
export class EventService {

  eventList = [];
  items: AngularFireList<any[]>;
  item: AngularFireObject<any>;
  constructor(db: AngularFireDatabase,private http:HttpClient) {
    // this.items = db.list('events');
    // this.item = db.object('/events/');
  }
  init() {
    // for(let thing in this.items) {
    //   console.log(thing);
    // }
    this.http.get('https://eventmode-7f117.firebaseio.com/events.json',{}).subscribe(responseData => {
      console.log("INITIALIZING EVENTSERVICE.");
      console.log(JSON.parse(JSON.stringify(responseData)));
      this.eventList = JSON.parse(JSON.stringify(responseData));
      for(let event in this.eventList) {
        if(event['title'] == null) {
          this.eventList.shift();
        }
      }
      // console.log(this.eventList[0]);
      // for(let item in responseData) {
      //   // this.eventList.push(responseData);
      // }
      })
  
  }
  getEvents() {
    return this.eventList;
  }
}
