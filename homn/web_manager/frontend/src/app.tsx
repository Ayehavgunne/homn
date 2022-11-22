import type { Component } from "solid-js"
import { A, Route, Routes } from "@solidjs/router"

import Login from "./pages/login/login"
import Index from "./pages/index/index"

import styles from "./app.module.sass"

const App: Component = () => {
	return (
		<div class={styles.app}>
			<header class={styles.header}>Homn</header>
			<nav class={styles.nav}>
				<A href="/login" class={styles.link}>
					Log In
				</A>
				<A href="/" class={styles.link}>
					Home
				</A>
			</nav>
			<main class={styles.main}>
				<Routes>
					<Route path={"/"} component={Index}></Route>
					<Route path={"/login"} component={Login}></Route>
				</Routes>
			</main>
		</div>
	)
}

export default App
