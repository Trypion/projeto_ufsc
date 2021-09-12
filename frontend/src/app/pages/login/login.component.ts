import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/services/auth.service';
import { User } from '../../models/user.model';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent implements OnInit {
  loginForm = new FormGroup({
    login: new FormControl('', Validators.required),
    password: new FormControl('', Validators.required),
  });

  getErrorMessage() {
    if (this.loginForm.hasError('required')) {
      return 'Não pode estar em branco';
    }

    return this.loginForm.hasError('login') ? 'este login não é valido' : 'está senha não é valida';
  }

  constructor(
    private location: Location,
    private auth: AuthService,
    private router: Router
  ) {}

  ngOnInit(): void {}

  onSubmit(): void {}

  login() {}
}
