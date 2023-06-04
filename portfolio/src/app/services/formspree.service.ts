import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

export interface IContactFormMessage {
  name: string;
  email: string;
  message: string;
}

const FORMSPREE_ENDPOINT = 'https://formspree.io/f/xzbqlrjb';

@Injectable({
  providedIn: 'root',
})
export class FormspreeService {
  constructor(private http: HttpClient) {}

  sendMessage(value: IContactFormMessage): Observable<any> {
    return this.http.post<any>(FORMSPREE_ENDPOINT, value);
  }
}
