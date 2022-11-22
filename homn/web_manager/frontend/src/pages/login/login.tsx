import type { Component } from "solid-js"

import styles from "./login.module.sass"

let Login: Component = () => {
	return (
		<form action="/auth" method="post" class={styles.form}>
			<h3>Login</h3>
			<label class={styles.label}>
				Username:
				<input name="username" />
			</label>
			<label class={styles.label}>
				Password:
				<input type="password" name="password" />
			</label>
			<input type="submit" value="Login" />
		</form>
	)
}

export default Login
