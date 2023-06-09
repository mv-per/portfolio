import { Component, HostListener, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  encapsulation: ViewEncapsulation.None,
})
export class AppComponent {
  headerFixed = false;

  @HostListener('window:scroll', ['$event'])
  protected onScroll() {
    if (window.scrollY > 80) {
      this.headerFixed = true;
    } else {
      this.headerFixed = false;
    }
  }
}
