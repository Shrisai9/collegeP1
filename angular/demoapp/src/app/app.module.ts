import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    // your components
    AppComponent
  ],
  imports: [
    HttpClientModule, // Import this
    // other modules
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
