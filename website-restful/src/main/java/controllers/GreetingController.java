package controllers;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.QueryParam;
import javax.ws.rs.core.Application;

@Path("/greeting")
public class GreetingController extends Application {
	@GET
	public String returnName(@QueryParam("name") String name){
		return name+"TEST";
	}
}
