package renderers;

import javax.faces.component.UIComponent;
import javax.faces.context.FacesContext;
import javax.faces.context.ResponseWriter;

import com.sun.faces.renderkit.html_basic.TextRenderer;

//Code by mb.akturk (http://stackoverflow.com/a/11416458)
public class MyInputTextRenderer extends TextRenderer {
	   @Override
	    protected void getEndTextToRender(FacesContext context,
	            UIComponent component,
	            String currentValue)
	     throws java.io.IOException{

	        String [] attributes = {"data-validate-complexity","data-confirmation-field"};

	        ResponseWriter writer = context.getResponseWriter();

	        for(String attribute : attributes)
	        {
	            String value = (String)component.getAttributes().get(attribute);
	            if(value != null) {                             
	                writer.writeAttribute(attribute, value, attribute);
	            }
	        }

	        super.getEndTextToRender(context, component, currentValue);

	    }
}