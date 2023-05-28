import {
  ChangeDetectionStrategy,
  ChangeDetectorRef,
  Component,
  ElementRef,
  HostListener,
  OnDestroy,
  OnInit,
} from '@angular/core';
import { faArrowUp } from '@fortawesome/free-solid-svg-icons';
import { Subscription, fromEvent, map, tap } from 'rxjs';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class HomeComponent {
  upperIcon = faArrowUp;

  @HostListener('window:scroll')
  onScrollChanged() {
    this.scrollChanged(window.scrollY);
  }

  scrollChanged(position: number): void {
    if (position > 500) {
      this.showGoToTopButton(true);
    } else {
      this.showGoToTopButton(false);
    }
  }

  goToTop() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
  }

  showGoToTopButton(display: boolean): void {
    if (display) {
      document.getElementById('goToTop')?.style.setProperty('display', 'block');
    } else {
      document.getElementById('goToTop')?.style.setProperty('display', 'none');
    }
  }
}
