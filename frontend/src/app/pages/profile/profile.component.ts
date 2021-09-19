import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { Course } from 'src/app/models/course.model';
import { Profile } from 'src/app/models/profile.model';
import { University } from 'src/app/models/university.model';
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

  universities: Array<University> = [];
  courses: Array<Course> = [];
  profile_id = ""

  ngOnInit(): void {
    this.profile_id = localStorage.getItem('profile_id') || "";

    this.getProfileById(this.profile_id);
    this.getUniversities();
  }

  onSubmit(): void {
    if (this.profileForm.valid) {
      const profile: Profile = this.profileForm.value;
      profile.id = this.profile_id
      profile.profile_picture = ""
      this.httpService.updateProfile(profile).subscribe((profile) => {
        const {
          name,
          email,
          sex,
          age,
          course,
          university,
          university_register,
        } = profile;
        this.profileForm.setValue({
          name,
          email,
          sex,
          age,
          course,
          university,
          university_register,
        });
      });
    }
  }

  getProfileById(id: string) {
    this.httpService.getProfileById(id).subscribe((profile) => {
      const { name, email, sex, age, course, university, university_register } =
        profile;
      this.getCoursesByUniversity(university);
      this.profileForm.setValue({
        name,
        email,
        sex,
        age,
        course,
        university,
        university_register,
      });
    });
  }

  getUniversities(): void {
    this.httpService.getAllUniversities().subscribe((universities) => {
      this.universities = universities;
    });
  }
  getCoursesByUniversity(id: string): void {
    this.httpService
      .getCourseByUniversity(id)
      .subscribe((courses) => (this.courses = courses));
  }
}
