import { Component, OnInit } from '@angular/core';
import { EventService } from 'app/event.service';

@Component({
  selector: 'app-table-list',
  templateUrl: './table-list.component.html',
  styleUrls: ['./table-list.component.css']
})
export class TableListComponent implements OnInit {
  eventList = [];
  constructor(public eventService:EventService) {
    this.eventList = this.eventService.eventList;

   }

  ngOnInit() {
    this.eventList = this.eventService.eventList;
  }

}
