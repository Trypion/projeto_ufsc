import {
  HttpClient,
  HttpErrorResponse,
  HttpHeaders,
} from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, throwError } from 'rxjs';
import { catchError, retry, tap } from 'rxjs/operators';
import { environment } from 'src/environments/environment';
import { User } from '../models/user.model';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  constructor(private httpClient: HttpClient) {}

  url = environment.apiUrl;

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' }),
  };

  //registra um usuario
  registerUser(user: User): Observable<{ id: string }> {
    return this.httpClient
      .post<{ id: string }>(
        `${this.url}/v1/user`,
        JSON.stringify(user),
        this.httpOptions
      )
      .pipe(retry(2), catchError(this.handleError));
  }

  //login um usuario
  login(user: User): Observable<{ token: string }> {
    return this.httpClient
      .post<{ token: string }>(
        `${this.url}/v1/login`,
        JSON.stringify(user),
        this.httpOptions
      )
      .pipe(
        retry(2),
        tap((val) => {
          localStorage.setItem('token', val.token);
        }),
        catchError(this.handleError)
      );
  }

  logout() {
    localStorage.removeItem('token');
  }

  handleError(error: HttpErrorResponse) {
    let errorMessage = '';
    if (error.error instanceof ErrorEvent) {
      // Erro ocorreu no lado do client
      errorMessage = error.error.message;
    } else {
      const { error: errMsg } = error.error;
      // Erro ocorreu no lado do servidor
      errorMessage =
        `Código do erro: ${error.status}, ` + `menssagem: ${errMsg}`;
    }
    console.log(errorMessage);
    return throwError(errorMessage);
  }
}
