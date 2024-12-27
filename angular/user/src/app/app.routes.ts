import { PreloadAllModules, RouterModule, Routes } from '@angular/router';
import { UserComponent } from './components/user/user.component';
import { NgModule } from '@angular/core';

export const routes: Routes = [
    { path: '', pathMatch: 'full', component: UserComponent, }
];


@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule],
    providers: []
  })
  export class AppRoutingModule { }