import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

const GIT_HUB_USER_URL = 'https://api.github.com/users/mv-per';
const GIT_HUB_BASE_URL = 'https://api.github.com';

@Injectable({
  providedIn: 'root',
})
export class GithubService {
  constructor(private http: HttpClient) {}

  getInfo() {
    return this.http.get<any>(GIT_HUB_USER_URL);
  }
  getRepositories() {
    return this.http.get<any>(GIT_HUB_USER_URL + '/repos');
  }

  getRepositoryLanguages(repository: string) {
    return this.http.get<any>(
      GIT_HUB_BASE_URL + '/repos/mv-per' + `/${repository}` + '/languages'
    );
  }
}
