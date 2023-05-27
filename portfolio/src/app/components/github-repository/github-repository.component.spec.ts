import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GithubRepositoryComponent } from './github-repository.component';

describe('GithubRepositoryComponent', () => {
  let component: GithubRepositoryComponent;
  let fixture: ComponentFixture<GithubRepositoryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GithubRepositoryComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(GithubRepositoryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
