import type { Component } from "solid-js"

import style from "./login.module.css"

let Login: Component = () => {
	return (
		<form action="/auth" method="post" style={style.login}>
			<label>
				Username:
				<input type="username" name="username" />
			</label>
			<label>
				Password:
				<input type="password" name="password" />
			</label>
			<input type="submit" value="Login" />
		</form>
	)
}

export default Login
