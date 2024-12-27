import { NgModule } from "@angular/core";
import { AppComponent } from "./app.component";
import { BrowserModule } from "@angular/platform-browser";
import { HttpClient } from "@angular/common/http";
import { AppRoutingModule } from "./app-routing.module";
import { UserComponent } from "./components/user/user.component";

@NgModule({
    declarations: [AppComponent, UserComponent],
    imports: [BrowserModule, AppRoutingModule, HttpClient],
    providers: [],
    bootstrap: [AppComponent]
})

export class AppModule {}