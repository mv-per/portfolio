import { ChangeDetectorRef, Component } from '@angular/core';
import { EMPTY, catchError, map, tap } from 'rxjs';
import { GithubService } from 'src/app/services/github.service';

const UNWANTED_REPOSITORIES = ['mv-per', 'portfolio', 'JS-scripts'];

interface IRepository {
  name: string;
}

@Component({
  selector: 'app-projects',
  templateUrl: './projects.component.html',
  styleUrls: ['./projects.component.scss'],
  providers: [GithubService],
})
export class ProjectsComponent {
  repositories: any;
  height: number = 0;
  errorMessage: string = '';

  constructor(
    private gitHubService: GithubService,
    private changeDetector: ChangeDetectorRef
  ) {}

  ngOnInit(): void {
    this.gitHubService
      .getRepositories()
      .pipe(
        catchError((err) => {
          this.errorMessage = 'Error Fetching Repositories';
          console.error(err);
          return EMPTY;
        }),
        map((repositories) => {
          return repositories.filter(
            (repository: IRepository) =>
              UNWANTED_REPOSITORIES.indexOf(repository['name']) === -1
          );
        }),

        tap((data) => {
          this.repositories = data.sort(
            (x: any, y: any) =>
              +new Date(y.updated_at) - +new Date(x.updated_at)
          );
        })
      )
      .subscribe();
    this.height = window.innerHeight;
    this.changeDetector.detectChanges();
  }
}
