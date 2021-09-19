import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { Event } from 'src/app/models/event.model';
import { HttpService } from 'src/app/services/http.service';

@Component({
  selector: 'app-event-create',
  templateUrl: './event-create.component.html',
  styleUrls: ['./event-create.component.css']
})
export class EventCreateComponent implements OnInit {
  constructor(private httpService: HttpService, private router: Router) { }

  ngOnInit(): void {
  }

  eventForm = new FormGroup({
    name: new FormControl('', Validators.required),
    start_at: new FormControl('', Validators.required),
    end_at: new FormControl('', Validators.required),
    description: new FormControl('', Validators.required),
    location: new FormControl('', Validators.required),
    reward: new FormControl('', Validators.required)
  })


  onSubmit(){
    let event: Event = this.eventForm.value;
    if (this.eventForm.valid) {
      event.event_picture = ""
      console.log(event)
      this.httpService.createEvent(event).subscribe(
        (event) => {
          this.router.navigateByUrl(`/event/${event.id}`)
        },
      );
    }
  }

}
