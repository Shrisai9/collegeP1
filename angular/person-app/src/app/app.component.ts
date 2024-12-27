import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';  // Import FormsModule
import { firstValueFrom } from 'rxjs/internal/firstValueFrom';

@Component({
  selector: 'app-root',
  standalone: true,  // Ensure the component is marked as standalone
  imports: [FormsModule],  // Import FormsModule here
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  people: any[] = [];
  newPerson: any = { name: '', age: 0, gender: '', mobile: '' };
  apiUrl: any;
  http: any;
  oUserService: any;

  addPerson() {
    this.people.push({ ...this.newPerson });
    this.newPerson = { name: '', age: 0, gender: '', mobile: '' }; // Reset form
  }
  adduser(){
    let req={
      "name": "Rahul",
      "email": "rahul@example.com",
      "password": "123456"
    }
    this.oUserService.addUser(req).then((Response : any) =>{
      console.log(Response);
    })

  }
}
