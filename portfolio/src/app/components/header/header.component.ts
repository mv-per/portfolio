import {
  Component,
  OnInit,
  ChangeDetectionStrategy,
  HostListener,
} from '@angular/core';
import { faBars, faClose } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class HeaderComponent {
  barsIco = faBars;
  closeIco = faClose;
  _screenWidth!: number;
  showDropdown = false;
  shortLogoText = 'Marcus Pereira';

  headerLinks = [
    { route: '/about', name: 'About' } as IHeaderLink,
    { route: '/projects', name: 'Projects' } as IHeaderLink,
    { route: '/resume', name: 'Resume' } as IHeaderLink,
    { route: '/contact', name: 'Contact' } as IHeaderLink,
  ];

  set screenWidth(value: number) {
    if (value < 1024) {
      this.shortLogoText = 'MVP';
    } else {
      this.shortLogoText = 'Marcus Pereira';
    }
  }

  constructor() {
    this.screenWidth = window.innerWidth;
  }

  @HostListener('window:resize', ['$event'])
  onResize(event: IResizeEvent) {
    this.screenWidth = event.target.innerWidth;

    if (this.screenWidth > 767) {
      this.showDropdown = false;
    }
  }
}

interface IHeaderLink {
  route: string;
  name: string;
}

interface ITarget {
  innerWidth: number;
}
interface IResizeEvent {
  target: ITarget;
}
