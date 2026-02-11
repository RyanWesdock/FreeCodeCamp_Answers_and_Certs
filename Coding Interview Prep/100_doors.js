function getFinalOpenedDoors(numDoors) {
    const doors = [];
    for (let i = 1; i <= numDoors; i++) {
      for (let num = 1; num <= numDoors; num++) {
        if (doors.includes(num) == false && num % i == 0) {
          doors.push(num);
        } else if (doors.includes(num) && num % i == 0) {
            doors.splice(doors.indexOf(num), 1);

        } else {
          continue;
        }
      } 
    } return doors;
