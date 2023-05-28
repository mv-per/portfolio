import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { GithubService } from './services/github.service';
import { map, tap } from 'rxjs/operators';
import { faLinkedin, faGithub } from '@fortawesome/free-brands-svg-icons';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent {}
