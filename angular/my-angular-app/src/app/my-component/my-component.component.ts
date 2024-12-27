import { Component } from '@angular/core';

@Component({
  selector: 'app-root',  // 'app-my-component' for a new component
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'my-angular-app';

  // Function to be called in HTML
  showMessage(): string {
    return "Hello from Angular!";
  }
}
