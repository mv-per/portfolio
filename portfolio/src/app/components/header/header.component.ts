import { Component, OnInit, ChangeDetectionStrategy } from '@angular/core';
import {
  faGithub,
  faGithubSquare,
  faLinkedin,
  faLinkedinIn,
  faWhatsapp,
  faWhatsappSquare,
} from '@fortawesome/free-brands-svg-icons';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class HeaderComponent implements OnInit {
  linkedinIco = faLinkedinIn;
  githubIco = faGithubSquare;
  whatsappIco = faWhatsapp;
  GITHUB_WEB_URL = 'https://github.com/mv-per';
  LINKEDIN_WEB_URL = 'https://www.linkedin.com/in/marcusvpereira/';
  WHATSAPP_URL =
    'https://api.whatsapp.com/send?phone=5545999128303&text=Ol%C3%A1%20Marcus';
  constructor() {}

  ngOnInit(): void {}
}
