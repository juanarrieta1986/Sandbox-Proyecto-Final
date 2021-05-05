import React, { useContext } from "react";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.scss";

export const SendEmail = () => {
	const { store, actions } = useContext(Context);

	return (
		<div>
			<input type="button" value="Send Email" onClick={() => actions.sendEmail()} />
			<script>{actions.addEmailScript()}</script>
		</div>
	);
};
