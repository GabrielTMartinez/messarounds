package beans;

import java.io.Serializable;

import javax.faces.bean.ManagedBean;
import javax.faces.bean.SessionScoped;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@ManagedBean(name="user")
@SessionScoped
@Entity (name="user")
@Table (name="users", schema="mein1")
public class User implements Serializable {
	private static final long serialVersionUID = 1L;
	
	//private int id;
	private String name;
	//@ManagedProperty(value="#{pwd}")
	private char[] password;
	
	public User(){}
	
	@Id
	@Column (name="username")
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	
	@Column (name="pwd")
	public char[] getPassword() {
		return password;
	}
	
	public void setPassword(char[] password) {
		this.password = password;
	}
	
	public void setPassword(String password) {
		this.password = password.toCharArray();
	}

	/*@Id
	@Column (name="user_id")
	public int getUserId() {
		return userId;
	}

	public void setUserId(int userId) {
		this.userId = userId;
	}*/
}