import { ChangeDetectorRef, Component } from '@angular/core';
import { map, tap } from 'rxjs/operators';
import { GithubService } from 'src/app/services/github.service';

@Component({
  selector: 'app-welcome',
  templateUrl: './welcome.component.html',
  styleUrls: ['./welcome.component.scss'],
  providers: [GithubService],
})
export class WelcomeComponent {}
