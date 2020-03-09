let uc_variables = {
    nickname: "kl@dmen2007",
    profile_image_src: "/static/images/profile_image.jpg",
    user_achievements: "11010",
    creator_achievements: "01000"
};

function uc_init() {
    //set profile_image
    let profile_image = document.getElementById("profile_image");
    profile_image.src = uc_variables.profile_image_src;
    //set achievements
    let userAchievements = document.getElementById("player_achievements").childNodes;
    for (let i = 1; i < userAchievements.length; i += 2) {
        if (uc_variables.user_achievements[(i+1)/2-1] === "1") {
            userAchievements[i].classList.remove('not_completed');
            userAchievements[i].classList.add('completed');
        }
    }
    let creatorAchievements = document.getElementById("creator_achievements").childNodes;
    for (let i = 1; i < userAchievements.length; i += 2) {
        if (uc_variables.creator_achievements[(i + 1) / 2 - 1] === "1") {
            creatorAchievements[i].classList.remove('not_completed');
            creatorAchievements[i].classList.add('completed');
        }
    }
    //set nickname
    let nickname = document.getElementById("nickname");
    nickname.innerText = uc_variables.nickname;


}

export {uc_init}