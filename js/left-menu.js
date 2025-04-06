document.addEventListener("DOMContentLoaded", function () {
    // 1단계 메뉴 토글 (원래 방식으로 복구)
    const menuToggles = document.querySelectorAll(".menu-toggle");
    menuToggles.forEach(toggle => {
        toggle.addEventListener("click", function () {
            const submenu = this.nextElementSibling;
            if (submenu.style.display === "block") {
                submenu.style.display = "none";
            } else {
                submenu.style.display = "block";
            }
        });
    });

    // 2단계 메뉴(submenu-group) 토글
    const submenuGroups = document.querySelectorAll(".submenu-group");
    submenuGroups.forEach(group => {
        group.addEventListener("click", function(e) {
            e.stopPropagation(); // 상위 메뉴 토글 방지
            
            // 현재 그룹 다음에 오는 모든 li 요소들을 찾아서 토글
            let nextElement = this.nextElementSibling;
            while (nextElement && !nextElement.classList.contains("submenu-group")) {
                if (nextElement.style.display === "block") {
                    nextElement.style.display = "none";
                } else {
                    nextElement.style.display = "block";
                }
                nextElement = nextElement.nextElementSibling;
            }
        });
    });
});
