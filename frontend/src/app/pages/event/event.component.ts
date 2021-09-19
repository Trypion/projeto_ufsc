import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import { Event } from 'src/app/models/event.model';
import { HttpService } from 'src/app/services/http.service';

@Component({
  selector: 'app-event',
  templateUrl: './event.component.html',
  styleUrls: ['./event.component.css'],
})
export class EventComponent implements OnInit {
  constructor(
    private route: ActivatedRoute,
    private httpService: HttpService
  ) {}

  ngOnInit(): void {
    this.route.params.subscribe((params) => {
      const id = params['id'];
      this.getEventById(id);
    });
  }

  getEventById(id: string) {
    this.httpService.getEventById(id).subscribe((event) => {
      const { name, start_at, end_at, description, location, reward } = event;
      this.eventForm.setValue({
        name,
        start_at,
        end_at,
        description,
        location,
        reward,
      });
    });
  }

  eventForm = new FormGroup({
    name: new FormControl('', Validators.required),
    start_at: new FormControl('', Validators.required),
    end_at: new FormControl('', Validators.required),
    description: new FormControl('', Validators.required),
    location: new FormControl('', Validators.required),
    reward: new FormControl('', Validators.required),
  });

  onSubmit() {
    let event: Event = this.eventForm.value;
    if (this.eventForm.valid) {
      event.event_picture = '';
      console.log(event);
      this.httpService.createEvent(event).subscribe((event) => {});
    }
  }
}
