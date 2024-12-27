import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { firstValueFrom } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UsersService {

  private apiUrl = 'http://localhost:3000/api/users'; // Your Node.js API URL

  constructor(private http: HttpClient) { }

  // Method to get all users
  async getUsers() {
    let res: any = null;
    await firstValueFrom(this.http.get(this.apiUrl)).then((response: any) => {
      res = response;
    });
    return res;
  }

  async addUser(req: any) {
    let res: any = null;
    await firstValueFrom(this.http.post(this.apiUrl, req)).then((response: any) => {
      res = response;
    });
    return res;
  }
}
