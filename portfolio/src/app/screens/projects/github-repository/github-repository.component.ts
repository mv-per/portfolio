import {
  AfterViewInit,
  ChangeDetectorRef,
  Component,
  Input,
  OnInit,
} from '@angular/core';
import { catchError, EMPTY, map, Observable, tap } from 'rxjs';
import { GithubService } from 'src/app/services/github.service';
import { ChartType } from 'chart.js';
import { HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-github-repository',
  templateUrl: './github-repository.component.html',
  styleUrls: ['./github-repository.component.scss'],
  providers: [GithubService],
})
export class GithubRepositoryComponent implements OnInit {
  @Input() repository: any;

  totalBytes = 0;
  data: any = {
    labels: [],
    datasets: [{ data: [], backgroundColor: [], hoverBackgroundColor: [] }],
  };

  lastUpdateDate?: string;
  doughnutChartType: ChartType = 'doughnut';
  repositoryTitle?: string;
  showGraph = false;

  constructor(
    private gitHubService: GithubService,
    private changeDetector: ChangeDetectorRef
  ) {}

  ngOnInit(): void {
    this.repositoryTitle = this.repository.name.split(/[-_ ]/g).join(' ');
    this.lastUpdateDate = new Date(
      this.repository.updated_at
    ).toLocaleDateString();
    this.gitHubService
      .getRepositoryLanguages(this.repository.name)
      .pipe(
        catchError((err: HttpErrorResponse) => {
          console.error(err);
          return EMPTY;
        }),
        tap((res) => {
          this.setupGraphData(res);
          this.changeDetector.detectChanges();
        })
      )
      .subscribe();
  }

  setupGraphData(languages: any) {
    this.totalBytes = 0;
    for (let k in languages) {
      this.totalBytes = this.totalBytes + languages[k];
    }

    for (let k in languages) {
      this.data.labels.push(k);
      this.data.datasets[0].data.push((languages[k] / this.totalBytes) * 100);
      this.data.datasets[0].backgroundColor.push(this.getLanguageColor(k));
      this.data.datasets[0].hoverBackgroundColor.push(this.getLanguageColor(k));
    }

    this.showGraph = true;
  }

  getLanguageColor(language: string) {
    if (language === 'Python') {
      return '#FFdb58';
    } else if (language === 'C') {
      return '#5b92e5';
    } else if (language === 'C++') {
      return '#191970';
    } else if (language === 'HTML') {
      return '#ff6e4a';
    } else if (language === 'JavaScript') {
      return '#0abab5';
    } else {
      return '#bcd4e6';
    }
  }
}
