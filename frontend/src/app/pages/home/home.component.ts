import { Component, OnInit } from '@angular/core';
import { Event } from 'src/app/models/event.model';
import { HttpService } from 'src/app/services/http.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
})
export class HomeComponent implements OnInit {
  constructor(private httpService: HttpService) {}

  events: Array<Event> = [];

  ngOnInit(): void {
    this.getAllEvents();
  }

  getAllEvents() {
    this.httpService.getAllEvents().subscribe((events) => {
      this.events = events;
      console.log(this.events)
    });
  }
}
