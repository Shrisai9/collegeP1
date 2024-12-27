import { Component } from '@angular/core';
import { UsersService } from '../../services/users.service';

@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrl: './user.component.css'
})
export class UserComponent {
  
  constructor(private oUserService : UsersService){}
  
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
