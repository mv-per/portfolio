import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import {
  FormspreeService,
  IContactFormMessage,
} from 'src/app/services/formspree.service';

@Component({
  selector: 'app-contact-form',
  templateUrl: './contact-form.component.html',
  styleUrls: ['./contact-form.component.scss'],
  providers: [FormspreeService],
})
export class ContactFormComponent {
  name = new FormControl('');

  contactForm = new FormGroup({
    name: new FormControl('', [Validators.required]),
    email: new FormControl('', [Validators.required, Validators.email]),
    message: new FormControl('', [Validators.required]),
  });

  sendingMessage = false;

  constructor(public formspreeService: FormspreeService) {}

  onSubmit() {
    const value = this.contactForm.value as IContactFormMessage;
    this.sendingMessage = true;
    this.formspreeService.sendMessage(value).subscribe(
      (response) => console.log(response),
      (err) => console.log(err)
    );
  }
}
