const {
    prisma
} = require('../prisma-client');

async function main() {


    await prisma.createUser({
        username: 'Alice',
        email: 'alice@prisma.io',
        password: 'alice',

    });


}

main();
