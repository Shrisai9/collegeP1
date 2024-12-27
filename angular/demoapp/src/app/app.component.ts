import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { UserService } from './user.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'demoapp';
  userData: any = [];

  constructor(private oUserService : UserService) {}

  ngOnInit() {
    this.oUserService.getUsers().then((response: any) => {
      this.userData = response;
    });
  }

}
