import type { Component } from "solid-js"
import { Route, Routes } from "@solidjs/router"

import Login from "./pages/login/login"

import styles from "./App.module.css"

const App: Component = () => {
	return <div class={styles.App}>
		<Routes>
			<Route path={"/login"} component={Login}></Route>
		</Routes>
	</div>
}

export default App
