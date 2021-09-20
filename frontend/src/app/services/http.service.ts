import {
  HttpClient,
  HttpErrorResponse,
  HttpHeaders,
  HttpParams,
} from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, throwError } from 'rxjs';
import { catchError, retry, tap } from 'rxjs/operators';
import { environment } from 'src/environments/environment';
import { Course } from '../models/course.model';
import { Event } from '../models/event.model';
import { Profile } from '../models/profile.model';
import { University } from '../models/university.model';

export interface Search {
  from: Date;
  to: Date;
  name: string;
}

@Injectable({
  providedIn: 'root',
})
export class HttpService {
  constructor(private httpClient: HttpClient) {}

  url = environment.apiUrl;

  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json',
      Authorization: localStorage.getItem('token') || '',
    }),
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

  getCourseByUniversity(id: string): Observable<Array<Course>> {
    return this.httpClient
      .get<Array<Course>>(
        `${this.url}/v1/course/${id}/university`,
        this.httpOptions
      )
      .pipe(
        retry(2),
        tap((val) => {}),
        catchError(this.handleError)
      );
  }

  getProfileById(id: string): Observable<Profile> {
    return this.httpClient
      .get<Profile>(`${this.url}/v1/profile/${id}`, this.httpOptions)
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

  updateProfile(profile: Profile): Observable<Profile> {
    return this.httpClient
      .put<Profile>(
        `${this.url}/v1/profile/${profile.id}`,
        profile,
        this.httpOptions
      )
      .pipe(
        retry(2),
        tap((val) => {
          localStorage.setItem('profile_name', val.name);
        }),
        catchError(this.handleError)
      );
  }

  createEvent(event: Event): Observable<Event> {
    return this.httpClient
      .post<Event>(
        `${this.url}/v1/event`,
        JSON.stringify(event),
        this.httpOptions
      )
      .pipe(
        retry(2),
        tap((val) => {}),
        catchError(this.handleError)
      );
  }

  getEventById(id: string): Observable<Event> {
    return this.httpClient
      .get<Event>(`${this.url}/v1/event/${id}`, this.httpOptions)
      .pipe(
        retry(2),
        tap((val) => {}),
        catchError(this.handleError)
      );
  }

  getAllEvents(): Observable<Array<Event>> {
    return this.httpClient
      .get<Array<Event>>(`${this.url}/v1/event`, this.httpOptions)
      .pipe(
        retry(2),
        tap((val) => {}),
        catchError(this.handleError)
      );
  }

  searchEvents(search: Search): Observable<Array<Event>> {
    const params = new HttpParams().set('name', search.name).set('from', search.from.toISOString()).set('to', search.to.toISOString())
    return this.httpClient.get<Array<Event>>(`${this.url}/v1/event/search`, {
      headers: this.httpOptions.headers,
      params: params,
    });
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
