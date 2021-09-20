import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Event } from 'src/app/models/event.model';
import { HttpService, Search } from 'src/app/services/http.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
})
export class HomeComponent implements OnInit {
  constructor(private httpService: HttpService) {}

  events: Array<Event> = [];

  searchForm = new FormGroup({
    from: new FormControl(''),
    to: new FormControl(''),
    name: new FormControl(''),
  });

  ngOnInit(): void {
    this.getAllEvents();
  }

  getAllEvents() {
    this.httpService.getAllEvents().subscribe((events) => {
      this.events = events;
    });
  }

  onSubmit(): void {
    if(this.searchForm.valid){
      const search: Search = this.searchForm.value
      this.httpService.searchEvents(search).subscribe((events)=>{
        this.events = events;
      })
    }
  }
}
