import { Component } from '@angular/core';
import { FormControl } from '@angular/forms';
import {
  faLinkedinIn,
  faGithubSquare,
  faWhatsapp,
} from '@fortawesome/free-brands-svg-icons';
import { faMailBulk } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-contact',
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.scss'],
})
export class ContactComponent {
  linkedinIco = faLinkedinIn;
  githubIco = faGithubSquare;
  whatsappIco = faWhatsapp;
  emailIco = faMailBulk;
  GITHUB_WEB_URL = 'https://github.com/mv-per';
  LINKEDIN_WEB_URL = 'https://www.linkedin.com/in/marcusvpereira/';
  WHATSAPP_URL =
    'https://api.whatsapp.com/send?phone=5545999128303&text=Ol%C3%A1%20Marcus';
}
