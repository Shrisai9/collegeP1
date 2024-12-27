import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  standalone: true  // Add this line
})
export class AppComponent {
  title = 'my-angular-app';

  showMessage(): string {
    return "Hello from Angular!";
  }
}
