import {
  HttpClient,
  HttpErrorResponse,
  HttpHeaders,
} from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, throwError } from 'rxjs';
import { catchError, retry, tap } from 'rxjs/operators';
import { environment } from 'src/environments/environment';
import { Profile } from '../models/profile.model';
import { University } from '../models/university.model';

@Injectable({
  providedIn: 'root',
})
export class HttpService {
  constructor(private httpClient: HttpClient) {}

  url = environment.apiUrl;

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' }),
  };

  getAllUniversities(): Observable<Array<University>> {
    return this.httpClient
      .get<Array<University>>(`${this.url}/v1/university`, this.httpOptions)
      .pipe(
        retry(2),
        tap((val) => {}),
        catchError(this.handleError)
      );
  }

  createProfile(profile: Profile): Observable<Profile> {
    return this.httpClient
      .post<Profile>(
        `${this.url}/v1/profile`,
        JSON.stringify(profile),
        this.httpOptions
      )
      .pipe(
        retry(2),
        tap((val) => {}),
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
