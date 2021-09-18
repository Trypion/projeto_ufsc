import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { Profile } from 'src/app/models/profile.model';
import { HttpService } from 'src/app/services/http.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css'],
})
export class ProfileComponent implements OnInit {
  profileForm = new FormGroup({
    sex: new FormControl('', Validators.required),
    age: new FormControl('', Validators.required),
    name: new FormControl('', Validators.required),
    email: new FormControl('', Validators.required),
    course: new FormControl('', Validators.required),
    university: new FormControl('', Validators.required),
    university_register: new FormControl('', Validators.required),
  });

  constructor(private httpService: HttpService, private router: Router) {}

  ngOnInit(): void {}

  onSubmit(): void {
    if (this.profileForm.valid) {
      const profile: Profile = this.profileForm.value;
      this.httpService.createProfile(profile).subscribe(() => {
        this.router.navigateByUrl('/home');
      });
    }
  }
}
