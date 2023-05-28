import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { GithubService } from './services/github.service';
import { GithubRepositoryComponent } from './components/github-repository/github-repository.component';
import { CommonModule } from '@angular/common';
import { NgChartsModule } from 'ng2-charts';
import { HttpClientModule } from '@angular/common/http';
import { RouterModule } from '@angular/router';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { ResumeComponent } from './screens/resume/resume.component';
import { WelcomeComponent } from './screens/welcome/welcome.component';
import { HeaderComponent } from './components/header/header.component';
import { PdfViewerModule } from 'ng2-pdf-viewer';
// import { NgxExtendedPdfViewerModule } from 'ngx-extended-pdf-viewer';
import { HomeComponent } from './screens/home/home.component';
import { ProjectsComponent } from './screens/projects/projects.component';

@NgModule({
  declarations: [
    AppComponent,
    GithubRepositoryComponent,
    ResumeComponent,
    WelcomeComponent,
    HeaderComponent,
    HomeComponent,
    ProjectsComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    CommonModule,
    RouterModule,
    HttpClientModule,
    NgChartsModule,
    FontAwesomeModule,
    PdfViewerModule,
    // NgxExtendedPdfViewerModule,
  ],
  providers: [GithubService],
  bootstrap: [AppComponent],
  exports: [],
})
export class AppModule {}
