import { THIS_EXPR } from '@angular/compiler/src/output/output_ast';
import { Component, OnInit } from '@angular/core';
import {
  AbstractControl,
  FormControl,
  FormGroup,
  FormGroupDirective,
  NgForm,
  ValidationErrors,
  ValidatorFn,
  Validators,
} from '@angular/forms';
import { ErrorStateMatcher } from '@angular/material/core';
import { Router } from '@angular/router';
import { Course } from 'src/app/models/course.model';
import { Profile } from 'src/app/models/profile.model';
import { University } from 'src/app/models/university.model';
import { User } from 'src/app/models/user.model';
import { AuthService } from 'src/app/services/auth.service';
import { HttpService } from 'src/app/services/http.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css'],
})
export class RegisterComponent implements OnInit {
  constructor(
    private authService: AuthService,
    private httpService: HttpService,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.getUniversities();
  }
  hide = true;
  universities: Array<University> = [];
  courses: Array<Course> = [];

  checkPasswords: ValidatorFn = (
    group: AbstractControl
  ): ValidationErrors | null => {
    const pass = group.get('password');
    const confirmPass = group.get('confirmPass');
    return pass && confirmPass && pass.value === confirmPass.value
      ? null
      : { notSame: true };
  };

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

  registerForm = new FormGroup({
    userForm: new FormGroup(
      {
        login: new FormControl('', Validators.required),
        password: new FormControl('', Validators.required),
        confirmPass: new FormControl('', Validators.required),
      },
      { validators: this.checkPasswords }
    ),
    profileForm: new FormGroup({
      sex: new FormControl('', Validators.required),
      age: new FormControl('', Validators.required),
      name: new FormControl('', Validators.required),
      email: new FormControl('', Validators.required),
      course: new FormControl('', Validators.required),
      university: new FormControl('', Validators.required),
      university_register: new FormControl('', Validators.required),
    }),
  });

  matcher = new MyErrorStateMatcher();

  onSubmit(): void {
    const user: User = this.registerForm.get('userForm')?.value;
    let profile: Profile = this.registerForm.get('profileForm')?.value;
    if (this.registerForm.valid) {
      this.authService.registerUser(user).subscribe((data) => {
        profile.user = data.id
        profile.profile_picture = ''
        this.httpService.createProfile(profile).subscribe(data =>{
          this.router.navigateByUrl('/login');
        })
      });
    }
  }
}

export class MyErrorStateMatcher implements ErrorStateMatcher {
  isErrorState(
    control: FormControl | null,
    form: FormGroupDirective | NgForm | null
  ): boolean {
    const invalidCtrl = !!(control?.invalid && control?.parent?.dirty);
    const invalidParent = !!(
      control?.parent?.invalid && control?.parent?.dirty
    );

    return invalidCtrl || invalidParent;
  }
}
