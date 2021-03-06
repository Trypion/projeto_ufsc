import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-nav-bar',
  templateUrl: './nav-bar.component.html',
  styleUrls: ['./nav-bar.component.css'],
})
export class NavBarComponent implements OnInit {
  name: string = '';

  constructor(private authService: AuthService, private router: Router) {}

  ngOnInit(): void {}

  isLoggedIn(): boolean {
    this.name = localStorage.getItem('profile_name') || "";
    return Boolean(localStorage.getItem('token'))
  }

  logout() {
    this.authService.logout();
    this.router.navigateByUrl('/home');
  }
}
