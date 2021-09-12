import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, throwError } from 'rxjs';
import { catchError, retry, tap } from 'rxjs/operators';
import { environment } from 'src/environments/environment';
import { User } from '../models/user.model';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private httpClient: HttpClient) { }

  url = environment.apiUrl

   // headers
   httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' }),
    withCredentials: true,
  };

  //alert options
  alertOptions = {
    autoClose: false,
    keepAfterRouteChange: true,
  };

  //registra um usuario
  registerUser(user: User): Observable<User> {
    return this.httpClient
      .post<User>(this.url, JSON.stringify(user), this.httpOptions)
      .pipe(
        retry(2),
        tap((val) => {sessionStorage.setItem("isLoggedIn", "true")}),
        catchError(this.handleError)
      );
  }

  //login um usuario
  login(user: User): Observable<boolean> {
    return this.httpClient
      .post<boolean>(
        this.url + '/login',
        JSON.stringify(user),
        this.httpOptions
      )
      .pipe(
        retry(2),
        tap((val) => {}),
        catchError(this.handleError)
      );
  }

  //logout um usuario
  logoutUser(): Observable<boolean> {
    return this.httpClient
      .get<boolean>(this.url + '/logout', this.httpOptions)
      .pipe(
        retry(2),
        tap((val) => {sessionStorage.setItem("isLoggedIn", "false")}),
        catchError(this.handleError)
      );
  }

  handleError(error: HttpErrorResponse) {
    let errorMessage = '';
    if (error.error instanceof ErrorEvent) {
      // Erro ocorreu no lado do client
      errorMessage = error.error.message;
    } else {
      // Erro ocorreu no lado do servidor
      errorMessage =
        `Código do erro: ${error.status}, ` + `menssagem: ${error.message}`;
    }
    console.log(errorMessage);
    return throwError(error);
  }

}
